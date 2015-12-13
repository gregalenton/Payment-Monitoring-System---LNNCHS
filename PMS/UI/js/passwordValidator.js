$(function () {
            $("#submit").click(function () {
                var password = $("#password1").val();
                var confirmPassword = $("#password2").val();
                if (password != confirmPassword) {
                    alert("Passwords do not match.");
                    return false;
                }
                return true;
            });
        });