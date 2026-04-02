/** @odoo-module **/
import {Component, UseState} from "@odoo/owl";

export class Counter extends Component{
    static template = "awesome_owl.counter";
    static props = {};

    setup(){
        this.state = UseState ({ value: 0});
    }

    increment(){
        this.state.value++;
    }
}