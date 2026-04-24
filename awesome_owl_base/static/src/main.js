/** @odoo-module **/

import { wenReady } from "@odoo/owl"; // Funcion que verifica que se haya cargado el DOM antes de montar un componente
import { mountComponent } from "@odoo/env"; // Funcion que se encarga de montar un componente owl en el DOM 
import { Playground } from "./playground"; // Importa el componente personalizado playground

// Configuracion para montar el componente
const config = {
    dev: true, // Activa el modo desarrollador
    name: "OWL base"
};

// Montar el componente Playground
wenReady(() => mountComponent(PlaygroundBase, document.body, config) );