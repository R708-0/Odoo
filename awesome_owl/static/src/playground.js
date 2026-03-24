/** @odoo-module **/
import { Component, useState } from "@odoo/owl";

// exporta la clase para que pueda ser usada por otro archivo
export class Playground extends Component {
    static template = "awesome_owl.Playground"; // debe coincidir con el t-name del template
    static props = {}; // para evitar warnings se crea un props(argumetos) vacio

    setup (){
        this.state = useState( {value: 0} ); // cuando cambie el valor de value se renderiza el template automaticamente
    }

    increment(){
        this.state.value++;
    }
}