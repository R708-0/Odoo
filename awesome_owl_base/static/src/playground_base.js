/** @odoo-module **/
import { Component, useState } from "@odoo/owl";

// exporta la clase para que pueda ser usada desde otro archivo
export class PlaygroundBase extends Component {
    static template= "awesome_owl.Playground_base"; // debe coincidir con el t-name del template
    static props = {}; // para evitar wrnings se crea un props(argumentos) vacio
}