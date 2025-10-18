/** @odoo-module **/

import { Component } from "@odoo/owl";

export  class MiComponente extends Component{
    static template = "awesome_owl.MiComponenteTemplate";

    setup() {
        this.saludo = "hola perrito";
    }
}