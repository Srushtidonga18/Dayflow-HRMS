const BASE_URL = "http://127.0.0.1:5000";

/* ---------------- LOGIN ---------------- */
async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const response = await fetch("http://127.0.0.1:5000/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const data = await response.json();

  if (response.ok) {
    localStorage.setItem("token", data.token);
    localStorage.setItem("role", data.role);
    localStorage.setItem("user_id", data.user_id);

    // 🔥 TEMP USER OBJECT (JUST FOR NOW)
    const user = {
      first_name: "Test",
      last_name: "User",
      email: email,
      employee_id: data.user_id,
      company_code: "DAYFLOW",
      role: data.role,
      year_of_joining: "2024"
    };

    localStorage.setItem("user", JSON.stringify(user));

    window.location.href = "employee_dashboard.html";
  } else {
    alert("Login failed");
  }
}


/* ---------------- SIGNUP ---------------- */
async function signup() {

  function signup() {
  const user = {
    firstName: document.getElementById("firstName").value,
    lastName: document.getElementById("lastName").value,
    employeeId: document.getElementById("employeeId").value,
    companyCode: document.getElementById("companyCode").value,
    email: document.getElementById("email").value,
    role: document.getElementById("role").value,
    yearOfJoining: document.getElementById("yearOfJoining").value
  };

  // save user data
  localStorage.setItem("user", JSON.stringify(user));

  alert("Signup successful!");
  window.location.href = "login.html";
}

  const payload = {
    employee_id: document.getElementById("employee_id").value,
    company_code: document.getElementById("company_code").value,
    first_name: document.getElementById("first_name").value,
    last_name: document.getElementById("last_name").value,
    email: document.getElementById("email").value,
    phone: document.getElementById("phone").value,
    password: document.getElementById("password").value,
    role: "EMPLOYEE",
    year_of_joining: new Date().getFullYear()
  };

  const response = await fetch(`${BASE_URL}/auth/signup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  const data = await response.json();
  alert(data.message);

  if (response.ok) {
    window.location.href = "login.html";
  }
}


/* ---------------- LOGOUT ---------------- */
function logout() {
  localStorage.clear();
  window.location.href = "login.html";
}
