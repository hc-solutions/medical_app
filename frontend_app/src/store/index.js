import { createStore } from "vuex";

import patients from "./patients/module.js";
import doctors from "./doctors/module.js";
import analyzes from "./analyzes/module.js";


export default createStore({
  modules: {
    patients,
    doctors,
    analyzes,
  }
})