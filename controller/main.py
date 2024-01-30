from odoo import http
from odoo.http import request


class GrievanceWebsiteForm(http.Controller):
    @http.route(['/grievance_form'], type='http', auth="public", website=True, csrf=False)
    def grievance_form(self):
        type = request.env['grievance.form.type'].sudo().search([])
        values = {
            'type': type
        }
        return request.render("grievance_form.grievance_online_form", values)

    @http.route(['/grievance_form/submit'], type='http', auth="public", website=True, csrf=False)
    def grievance_form_submit(self, **kw):
        print(kw, 'ooo')

        request.env['grievance.form'].sudo().create({
            'name': kw.get('name'),
            'batch': kw.get('batch'),
            'type': kw.get('type'),
            'mode_of_study': kw.get('mode_of_study'),
            'description': kw.get('description'),
            'priority': kw.get('priority'),
            'expected_resolution_date': kw.get('expecting_closing'),
            'type_of_issue': kw.get('type_of_issue'),

        })
        type = request.env['grievance.form.type'].sudo().search([('id', '=', kw.get('type_of_issue'))])
        activity = request.env['grievance.form'].sudo().search([], order='id desc', limit=1)
        print(activity.name, 'activity')

        activity.activity_schedule('grievance_form.mail_activity_grievance_form', res_id=activity.id, user_id=type.assigned_to.id,
                            note=f'This batch grievance added.')
        if type.assigned_to_users:
            for user in type.assigned_to_users:
                activity.activity_schedule('grievance_form.mail_activity_grievance_form', res_id=activity.id,
                                           user_id=user.id,
                                           note=f'This batch grievance added.')

        #
        return request.render("grievance_form.tmp_grievance_form_success", {})
