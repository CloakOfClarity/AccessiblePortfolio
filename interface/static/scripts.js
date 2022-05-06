function getBasic()
{ // This function will populate the fields on the home page
	$.get("/api", function(data,status)
	{
		$("#txtName").val(data.name);
		$("#txtPhone").val(data.phone);
		$("#txtEmail").val(data.email);
		$("#txtDescription").val(data.description);
	}); // End AJAX get method
} // end getBasic function

function editBasic()
{ // This function will post the basic information to the API
	$.post("/api/",{
		name:$("#txtName").val(),
		phone:$("#txtPhone").val(),
		email:$("#txtEmail").val(),
		description:$("#txtDescription").val()
	}, function(data,status) {
		alert("Your details were updated successfully!");
	}).fail(function(textStatus) {
		alert("One or more of your inputs were invalid. Please try again.");
		document.write(JSON.stringify(textStatus));
	}); // End AJAX post method
} // End editBasic function

function listEducation()
{ // This function will populate the education list
// Make sure the list is empty
	$("main>ul").empty();
// Put the option to add education at the top of the list
	$("main>ul").append($("<li></li>"));
	$("main li").append($("<a></a>").attr({"href":"#","onclick":"addEducationPage()"}).text("Add New Education"));
// call the API to get the education list
	$.get("/api/education", function(data,status)
	{
// Loop through the returned items
		for (let i = 0; i < data.length; i++)
		{
// Add each item to the list as a hyperlink
			$("main>ul").append($("<li></li>"));
			$("main li:last").append($("<a></a>").attr({"href":"#","onclick":"editEducationPage("+data[i].id+")"}).text(data[i].diploma+" at "+data[i].institution));
		} // End for loop
	}); // End AJAX get method
} // end listEducation function

function addEducationPage()
{ // This function will configure the form so that a new education can be added
	$("h3").text("Add New Education");
	$("input").val("");
	$("#btnPost").text("Add");
	$("#btnPost").attr("onclick","addEducation()");
	$("#btnDelete").attr("disabled","");
} // End addEducationPage function

function addEducation()
{ // This function will post the education data to the API to add it as a new education item
	$.post("/api/education",{
		diploma:$("#txtDiploma").val(),
		institution:$("#txtInstitution").val(),
		startYear:$("#txtStartYear").val(),
		endYear:$("#txtEndYear").val()
	}, function(data,status) {
		alert("Education added successfully!");
// Add the new education to the list
		$("main>ul").append($("<li></li>"));
		$("main li:last").append($("<a></a>").attr({"href":"#","onclick":"editEducationPage("+data.id+")"}).text(data.diploma+" at "+data.institution));
// Reset the form so that a new education can be added
		addEducationPage();
	}).fail(function() {
		alert("One or more of your inputs were invalid. Please try again.");
	}); // End AJAX post method
} // End addEducation function

function editEducationPage(id)
{ // This function will configure the form so that the education with the specified ID can be edited
// Fetch the data for the selected education from the API
	$.get("/api/education/"+id, function(data,status) {
		$("h3").text("Edit Selected Education");
		$("#educationID").val(id);
		$("#txtDiploma").val(data.diploma);
		$("#txtInstitution").val(data.institution);
		$("#txtStartYear").val(data.startYear);
		$("#txtEndYear").val(data.endYear);
		$("#btnPost").text("Update");
		$("#btnPost").attr("onclick","editEducation()");
		$("#btnDelete").removeAttr("disabled");
	}); // End AJAX get method
} // End editEducationPage function

function editEducation()
{ // This function will put the education data to the API to update the existing education
	$.ajax({url:"/api/education/"+$("#educationID").val(),type:"put",data:{
		diploma: $("#txtDiploma").val(),
		institution: $("#txtInstitution").val(),
		startYear: $("#txtStartYear").val(),
		endYear: $("#txtEndYear").val()
	},success: function() {
		alert("Education updated successfully!");
		listEducation();
	},error:function(){
		alert("One or more of your inputs were invalid. Please try again.");
	}}); // End AJAX method
} // End editEducation function

function deleteEducation()
{ // This function will send a delete request to the API to delete an existing education
	if(confirm("Are you sure you wish to delete this education?")) {
		$.ajax({url:"/api/education/"+$("#educationID").val(),type:"delete",success: function() {
			alert("Education deleted successfully!");
			listEducation();
			addEducationPage();
		},error:function(){
			alert("One or more of your inputs were invalid. Please try again.");
		}}); // End AJAX method
	} // End confirmation block
} // End deleteEducation function

function listEmployment()
{ // This function will populate the employment list
// Make sure the list is empty
	$("main>ul").empty();
// Put the option to add employment at the top of the list
	$("main>ul").append($("<li></li>"));
	$("main li").append($("<a></a>").attr({"href":"#","onclick":"addEmploymentPage()"}).text("Add New Employment"));
// call the API to get the employment list
	$.get("/api/employment", function(data,status)
	{
// Loop through the returned items
		for (let i = 0; i < data.length; i++)
		{
// Add each item to the list as a hyperlink
			$("main>ul").append($("<li></li>"));
			$("main li:last").append($("<a></a>").attr({"href":"#","onclick":"editEmploymentPage("+data[i].id+")"}).text(data[i].role+" at "+data[i].workplace));
		} // End for loop
	}); // End AJAX get method
} // end listEmployment function

function addEmploymentPage()
{ // This function will configure the form so that a new employment can be added
	$("h3").text("Add New Employment");
	$("input").val("");
	$("textarea").val("");
	$("#btnPost").text("Add");
	$("#btnPost").attr("onclick","addEmployment()");
	$("#btnDelete").attr("disabled","");
} // End addEmploymentPage function

function addEmployment()
{ // This function will post the employment data to the API to add it as a new employment item
	$.post("/api/employment",{
		role:$("#txtRole").val(),
		workplace:$("#txtWorkplace").val(),
		startYear:$("#txtStartYear").val(),
		endYear:$("#txtEndYear").val(),
		responsibilities:$("#txtResponsibilities").val()
	}, function(data,status) {
		alert("Employment added successfully!");
// Add the new employment to the list
		$("main>ul").append($("<li></li>"));
		$("main li:last").append($("<a></a>").attr({"href":"#","onclick":"editEmploymentPage("+data.id+")"}).text(data.role+" at "+data.workplace));
// Reset the form so that a new employment can be added
		addEmploymentPage();
	}).fail(function() {
		alert("One or more of your inputs were invalid. Please try again.");
	}); // End AJAX post method
} // End addEmployment function

function editEmploymentPage(id)
{ // This function will configure the form so that the employment with the specified ID can be edited
// Fetch the data for the selected employment from the API
	$.get("/api/employment/"+id, function(data,status) {
		$("h3").text("Edit Selected Employment");
		$("#employmentID").val(id);
		$("#txtRole").val(data.role);
		$("#txtWorkplace").val(data.workplace);
		$("#txtStartYear").val(data.startYear);
		$("#txtEndYear").val(data.endYear);
		$("#txtResponsibilities").val(data.responsibilities);
		$("#btnPost").text("Update");
		$("#btnPost").attr("onclick","editEmployment()");
		$("#btnDelete").removeAttr("disabled");
	}); // End AJAX get method
} // End editEmploymentPage function

function editEmployment()
{ // This function will put the employment data to the API to update the existing employment
	$.ajax({url:"/api/employment/"+$("#employmentID").val(),type:"put",data:{
		role:$("#txtRole").val(),
		workplace:$("#txtWorkplace").val(),
		startYear:$("#txtStartYear").val(),
		endYear:$("#txtEndYear").val(),
		responsibilities:$("#txtResponsibilities").val()
	},success: function() {
		alert("Employment updated successfully!");
		listEmployment();
	},error:function(){
		alert("One or more of your inputs were invalid. Please try again.");
	}}); // End AJAX method
} // End editEmployment function

function deleteEmployment()
{ // This function will send a delete request to the API to delete an existing employment
	if(confirm("Are you sure you wish to delete this employment?")) {
		$.ajax({url:"/api/employment/"+$("#employmentID").val(),type:"delete",success: function() {
			alert("Employment deleted successfully!");
			listEmployment();
			addEmploymentPage();
		},error:function(){
			alert("One or more of your inputs were invalid. Please try again.");
		}}); // End AJAX method
	} // End confirmation block
} // End deleteEmployment function

function listReferences()
{ // This function will populate the references list
// Make sure the list is empty
	$("main>ul").empty();
// Put the option to add a reference at the top of the list
	$("main>ul").append($("<li></li>"));
	$("main li").append($("<a></a>").attr({"href":"#","onclick":"addReferencePage()"}).text("Add New Reference"));
// call the API to get the references list
	$.get("/api/references", function(data,status)
	{
// Loop through the returned items
		for (let i = 0; i < data.length; i++)
		{
// Add each item to the list as a hyperlink
			$("main>ul").append($("<li></li>"));
			$("main li:last").append($("<a></a>").attr({"href":"#","onclick":"editReferencePage("+data[i].id+")"}).text(data[i].name));
		} // End for loop
	}); // End AJAX get method
} // end listReference function

function addReferencePage()
{ // This function will configure the form so that a new reference can be added
	$("h3").text("Add New Reference");
	$("input").val("");
	$("#btnPost").text("Add");
	$("#btnPost").attr("onclick","addReference()");
	$("#btnDelete").attr("disabled","");
} // End addReferencePage function

function addReference()
{ // This function will post the reference data to the API to add it as a new reference item
	$.post("/api/references",{
		name:$("#txtName").val(),
		phone:$("#txtPhone").val(),
		email:$("#txtEmail").val(),
	}, function(data,status) {
		alert("Reference added successfully!");
// Add the new reference to the list
		$("main>ul").append($("<li></li>"));
		$("main li:last").append($("<a></a>").attr({"href":"#","onclick":"editReferencePage("+data.id+")"}).text(data.name));
// Reset the form so that a new reference can be added
		addReferencePage();
	}).fail(function() {
		alert("One or more of your inputs were invalid. Please try again.");
	}); // End AJAX post method
} // End addReference function

function editReferencePage(id)
{ // This function will configure the form so that the reference with the specified ID can be edited
// Fetch the data for the selected reference from the API
	$.get("/api/references/"+id, function(data,status) {
		$("h3").text("Edit Selected Reference");
		$("#referenceID").val(id);
		$("#txtName").val(data.name);
		$("#txtPhone").val(data.phone);
		$("#txtEmail").val(data.email);
		$("#btnPost").text("Update");
		$("#btnPost").attr("onclick","editReference()");
		$("#btnDelete").removeAttr("disabled");
	}); // End AJAX get method
} // End editReferencePage function

function editReference()
{ // This function will put the reference data to the API to update the existing reference
	$.ajax({url:"/api/references/"+$("#referenceID").val(),type:"put",data:{
		name:$("#txtName").val(),
		phone:$("#txtPhone").val(),
		email:$("#txtEmail").val(),
	},success: function() {
		alert("Reference updated successfully!");
		listReferences();
	},error:function(){
		alert("One or more of your inputs were invalid. Please try again.");
	}}); // End AJAX method
} // End editReference function

function deleteReference()
{ // This function will send a delete request to the API to delete an existing reference
	if(confirm("Are you sure you wish to delete this reference?")) {
		$.ajax({url:"/api/references/"+$("#referenceID").val(),type:"delete",success: function() {
			alert("Reference deleted successfully!");
			listReferences();
			addReferencePage();
		},error:function(){
			alert("One or more of your inputs were invalid. Please try again.");
		}}); // End AJAX method
	} // End confirmation block
} // End deleteReference function

function listSkills()
{ // This function will populate the skills list
// Make sure the list is empty
	$("main>ul").empty();
// Put the option to add skill at the top of the list
	$("main>ul").append($("<li></li>"));
	$("main li").append($("<a></a>").attr({"href":"#","onclick":"addSkillPage()"}).text("Add New Skill"));
// call the API to get the skills list
	$.get("/api/skills", function(data,status)
	{
		let p = ['','Beginner','Regular','Expert'];
// Loop through the returned items
		for (let i = 0; i < data.length; i++)
		{
// Add each item to the list as a hyperlink
			$("main>ul").append($("<li></li>"));
			$("main li:last").append($("<a></a>").attr({"href":"#","onclick":"editSkillPage("+data[i].id+")"}).text(data[i].name+" ("+p[data[i].proficiency]+")"));
		} // End for loop
	}); // End AJAX get method
} // end listSkill function

function addSkillPage()
{ // This function will configure the form so that a new skill can be added
	$("h3").text("Add New Skill");
	$("input").val("");
	$("select").val("");
	$("#btnPost").text("Add");
	$("#btnPost").attr("onclick","addSkill()");
	$("#btnDelete").attr("disabled","");
} // End addSkillPage function

function addSkill()
{ // This function will post the skill data to the API to add it as a new skill item
	$.post("/api/skills",{
		name:$("#txtName").val(),
		proficiency:$("#cboProficiency").val(),
	}, function(data,status) {
		alert("Skill added successfully!");
// Add the new skill to the list
		let p = ['','Beginner','Regular','Expert'];
		$("main>ul").append($("<li></li>"));
		$("main li:last").append($("<a></a>").attr({"href":"#","onclick":"editSkillPage("+data.id+")"}).text(data.name+" ("+p[data.proficiency]+")"));
// Reset the form so that a new skill can be added
		addSkillPage();
	}).fail(function() {
		alert("One or more of your inputs were invalid. Please try again.");
	}); // End AJAX post method
} // End addSkill function

function editSkillPage(id)
{ // This function will configure the form so that the skill with the specified ID can be edited
// Fetch the data for the selected skill from the API
	$.get("/api/skills/"+id, function(data,status) {
		$("h3").text("Edit Selected Skill");
		$("#skillID").val(id);
		$("#txtName").val(data.name);
		$("#cboProficiency").val(data.proficiency);
		$("#btnPost").text("Update");
		$("#btnPost").attr("onclick","editSkill()");
		$("#btnDelete").removeAttr("disabled");
	}); // End AJAX get method
} // End editSkillPage function

function editSkill()
{ // This function will put the skill data to the API to update the existing skill
	$.ajax({url:"/api/skills/"+$("#skillID").val(),type:"put",data:{
		name:$("#txtName").val(),
		proficiency:$("#cboProficiency").val(),
	},success: function() {
		alert("Skill updated successfully!");
		listSkills();
	},error:function(){
		alert("One or more of your inputs were invalid. Please try again.");
	}}); // End AJAX method
} // End editSkill function

function deleteSkill()
{ // This function will send a delete request to the API to delete an existing skill
	if(confirm("Are you sure you wish to delete this skill?")) {
		$.ajax({url:"/api/skills/"+$("#skillID").val(),type:"delete",success: function() {
			alert("Skill deleted successfully!");
			listSkills();
			addSkillPage();
		},error:function(){
			alert("One or more of your inputs were invalid. Please try again.");
		}}); // End AJAX method
	} // End confirmation block
} // End deleteSkill function
