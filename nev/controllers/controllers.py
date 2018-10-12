# -*- coding: utf-8 -*-
from odoo import http

class Nev(http.Controller):
    @http.route('/nev/nev/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/nev/nev/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('nev.listing', {
            'root': '/nev/nev',
            'objects': http.request.env['nev.nev'].search([]),
        })

    @http.route('/nev/nev/objects/<model("nev.nev"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('nev.object', {
            'object': obj
        })
