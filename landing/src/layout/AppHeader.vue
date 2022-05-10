<template>
    <header class="header-global position-absolute d-flex w-100">
        <div class="container container-xl p-2 d-flex flex-row align-items-center">
            <h1 class="display-4 text-white">medical app</h1>
            <ul class="navbar-nav ml-lg-auto flex-row">
                <li class="nav-item">
                    <base-button tag="a" href="#" type="default" size="m">Sign In</base-button>
                </li>
                <li class="nav-item">
                    <base-button tag="a" href="#" type="secondary" size="m">Sign Up</base-button>
                </li>
            </ul>
        </div>
    </header>
</template>
<script>
import BaseButton from "../components/BaseButton.vue";

export default {
  components: {
    BaseButton
}
};
</script>
<style>
.header-global {
    z-index: 999;
}
</style>
