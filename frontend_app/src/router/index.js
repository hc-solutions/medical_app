import { createRouter, createWebHashHistory } from "vue-router";

import Tests from "../views/tests/Tests.vue";
import AuthLayout from "@/layout/AuthLayout";

import Login from "../views/Login.vue";
import Register from "../views/Register.vue";

const routes = [
  {
    path: "/",
    redirect: "login",
    component: AuthLayout,
    children: [
      {
        path: "/login",
        name: "login",
        components: { default: Login },
      },
      {
        path: "/register",
        name: "register",
        components: { default: Register },
      },
      {
        path: "/tests",
        name: "tests",
        components: { default: Tests },
      },
    ],
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  linkActiveClass: "active",
  routes,
});

export default router;
