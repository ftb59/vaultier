Vaultier.ErrorGenericRoute = Ember.Route.extend({

    renderTemplate: function() {
        var tpl = this.get('controller.content.template');
        if (tpl) {
            this.render(tpl)
        } else {
            this.render('ErrorGeneric')
        }
    }

})

Vaultier.ErrorGenericController = Ember.Controller.extend({
    content: {
        title: 'Oooups! Error',
        message: ''
    }
});

Vaultier.ErrorGenericView = Ember.View.extend({
    templateName: 'Error/ErrorGeneric',
    layoutName: 'Error/Layout'
});

Vaultier.Error404View = Ember.View.extend({
    templateName: 'Error/Error404',
    layoutName: 'Error/Layout'
});



