function login() {
  fetch("http://127.0.0.1:5000/api/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: document.getElementById("email").value,
      password: document.getElementById("password").value
    })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      // 🔑 IMPORTANT
      localStorage.setItem("user", JSON.stringify(data.user));
      localStorage.setItem("token", data.token);

      window.location.href = "employee_dashboard.html";
    } else {
      alert("Invalid login");
    }
  });
}
