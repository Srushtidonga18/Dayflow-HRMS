function checkAuth() {
  const token = localStorage.getItem("token");

  // if (!token) {
  //   alert("Please login first");
  //   window.location.href = "login.html";
  // }
}

function showUserInfo() {
  const userId = localStorage.getItem("user_id");
  const role = localStorage.getItem("role");

  document.getElementById("userInfo").innerText =
    `User ID: ${userId} | Role: ${role}`;
}

window.onload = function () {
  checkAuth();
  showUserInfo();
};


// window.onload = function () {
//   const token = localStorage.getItem("token");

//   if (!token) {
//     alert("Please login first.");
//     window.location.href = "login.html";
//   }
// };
