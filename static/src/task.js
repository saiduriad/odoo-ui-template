/** @odoo-module **/

alert('he')

import { Component, useState } from "@odoo/owl";

class Counter extends Component {
    static template = "odoo_ui_template.Counter";

    setup() {
        state = useState({ value: 0 });
    }

    increment() {
        this.state.value++;
    }
}