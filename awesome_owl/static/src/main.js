import { whenReady } from "@odoo/owl"; // funcion que verifica que se haya cargado el DOM antes de montar un componente
import { mountComponent } from "@web/env"; // funcion que se encargar de montar un componente owl en el DOM 
import { Playground } from "./playground"; // importa el componente personalizado playground

// Configuracion para montar del componente 
const config = {
    dev: true, // Activa el modo desarrollador
    name: "OWL Tutorial"
};

// Montar en componente Playground
whenReady( () => mountComponent(Playground, document.body, config) )





