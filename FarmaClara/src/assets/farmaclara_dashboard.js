/** @odoo-module **/

import { registry } from 'web/core/registry';
import { registry } from 'web/core/utils/patch';

// servicio que controla los dashboards
const dashboardRegistry = registry.category("spreadsheet_dashboard");

// modificar el metodo getEntries para filtrar
patch( dashboardRegistry, "remove_invoicing_dashboard", {
    getEntries(){
        // obtener los dashboards originales
        const dashboards = this.super(...arguments);
        // filtrar facturacion
        return dashboards.filtrer(d => d.id !== "dashboard_invoicing")
    }
});