<template>
    <div class="container mt-5">
        <div class="action-prompt m-auto">
            <h3 class="text-center">REGISTER</h3>
            <hr>
            <form>
                <div class="form-floating mb-3">
                    <input type="firstname" class="form-control" id="floatingFirstname" placeholder="Your First name">
                    <label for="floatingName">First name</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="lastname" class="form-control" id="floatingLastname" placeholder="Your Last name">
                    <label for="floatingName">Last name</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="email" class="form-control" id="floatingEmail" placeholder="name@gmail.com">
                    <label for="floatingEmail">Email address</label>
                </div>
                 <div class="form-floating mb-3">
                    <input type="username" class="form-control" id="floatingUsername" placeholder="Username">
                    <label for="floatingUsername">Username</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                    <label for="floatingPassword">Password</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="password" class="form-control" id="floatingConfirmPassword" placeholder="Confirm Password">
                    <label for="floatingConfirmPassword">Confirm Password</label>
                </div>
                <button type="submit" class="btn-transparent btn btn-primary">Register</button>
            </form>
            <router-link class="text-center nav-link text-white" to="/login"><span>Allready have an
                    account?</span></router-link>
        </div>
    </div>
</template>

<style scoped>
.action-prompt {
    border: 1px solid white;
    border-radius: 12px;
    padding: 15px;
    height: 50%;
    width: 50%;
    position: relative;
    background: rgba(0, 0, 0, 0.4);
}

.btn-transparent {
    background: transparent;
    color: white;
    border-color: white;
}

.btn-transparent:hover {
    background: white;
    color: black;
}

.form-floating>label {
    color: black !important;
}
</style>