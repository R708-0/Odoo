/** @odoo-module **/

import { registry } from "@web/core/registry";
import { patch } from "@web/core/utils/patch";

// El servicio que gestiona los dashboards está en "spreadsheet_dashboard"
const actionRegistry = registry.category("actions");

// Parcheamos la acción para interceptar cuando se abre un dashboard
patch(actionRegistry, "custom_dashboard_patch", {
    get(actionName) {
        const result = super.get(actionName);

        // Interceptamos la acción que abre dashboards
        if (actionName === "spreadsheet_dashboard.ir_actions_dashboard_action") {
            const original = result;

            return async (env, action) => {
                // Ejecutamos la acción original
                const res = await original(env, action);

                // Aquí podemos inyectar modificaciones en tiempo real
                console.log("📊 Dashboard cargado:", action);

                // Ejemplo: modificar el título de la vista
                const header = document.querySelector(".o_spreadsheet_dashboard_header h1");
                if (header) {
                    header.textContent = "📌 Dashboard de Compras (Modificado con JS)";
                }

                return res;
            };
        }
        return result;
    },
});