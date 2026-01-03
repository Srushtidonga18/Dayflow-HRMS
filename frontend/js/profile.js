window.onload = function () {
  const userStr = localStorage.getItem("user");

  /*if (!userStr) {
    alert("Please login again");
    window.location.href = "login.html";
    return;
  }*/

  const user = JSON.parse(userStr);
  console.log("Loaded user:", user);

  document.getElementById("name").innerText =
    (user.first_name || "") + " " + (user.last_name || "");

  document.getElementById("email").innerText = user.email || "-";
  document.getElementById("employeeId").innerText = user.employee_id || "-";
  document.getElementById("companyCode").innerText = user.company_code || "-";
  document.getElementById("role").innerText = user.role || "-";
  document.getElementById("year").innerText = user.year_of_joining || "-";
};
