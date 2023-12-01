# -*- coding: utf-8 -*-
# from odoo import http


# class ArsHelloKernel(http.Controller):
#     @http.route('/ars_hello_kernel/ars_hello_kernel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ars_hello_kernel/ars_hello_kernel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ars_hello_kernel.listing', {
#             'root': '/ars_hello_kernel/ars_hello_kernel',
#             'objects': http.request.env['ars_hello_kernel.ars_hello_kernel'].search([]),
#         })

#     @http.route('/ars_hello_kernel/ars_hello_kernel/objects/<model("ars_hello_kernel.ars_hello_kernel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ars_hello_kernel.object', {
#             'object': obj
#         })
