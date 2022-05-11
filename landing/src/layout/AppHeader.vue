<template>
    <div>
        <header class="header-global position-absolute d-flex w-100">
            <div class="container container-xl p-2 d-flex flex-row align-items-center">
                <h1 class="display-4 text-white">medical app</h1>
                <ul class="navbar-nav ml-lg-auto flex-row">
                    <li class="nav-item">
                        <base-button tag="a" href="#" type="default" size="m" @click="modals.signinmodal = true">Sign In</base-button>
                    </li>
                    <li class="nav-item">
                        <base-button tag="a" href="#" type="secondary" size="m" @click="modals.signupmodal = true">Sign Up</base-button>
                    </li>
                </ul>
            </div>
        </header>
        <modal :show.sync="modals.signinmodal">
            <template slot="header">
                <h5>Sign In</h5>
            </template>
            <div class="form-group">
                <label for="emailInput"><strong>Email</strong></label>
                <base-input type="email" placeholder="email@example.com" id="emailInput"></base-input>
            </div>
            <div class="form-group">
                <label for="passwordInput"><strong>Password</strong></label>
                <base-input type="password" placeholder="password" id="passwordInput"></base-input>
            </div>
            <div class="text-center">
                <base-button type="default" size="m">Sign in</base-button>
            </div>
        </modal>
        <modal :show.sync="modals.signupmodal">
            <template slot="header">
                <h5>Sign Up</h5>
            </template>
            <div class="text-center">
                <base-button type="default" size="m">Sign up</base-button>
            </div>
        </modal>
    </div>
</template>
<script>
import BaseButton from "../components/BaseButton.vue";
import BaseInput from "../components/BaseInput.vue";
import Modal from "../components/Modal.vue";

export default {
  components: {
    BaseButton,
    BaseInput,
    Modal,
    },
    data() {
        return {
            modals: {
                signinmodal: false,
                signupmodal: false,
            }
        }
    }
    
};
</script>
<style>
.header-global {
    z-index: 999;
}
</style>
