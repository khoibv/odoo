# -*- coding: utf-8 -*-
from odoo import http

class NevMboController(http.Controller):
    @http.route('/nev-mbo/nev-mbo/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/nev-mbo/nev-mbo/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('nev-mbo.listing', {
            'root': '/nev-mbo/nev-mbo',
            'objects': http.request.env['nev-mbo.nev-mbo'].search([]),
        })

    @http.route('/nev-mbo/nev-mbo/objects/<model("nev-mbo.nev-mbo"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('nev-mbo.object', {
            'object': obj
        })
