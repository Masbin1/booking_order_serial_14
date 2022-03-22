from odoo import api, fields ,models


class BookingOrder(models.Model):
    _inherit = 'sale.order'

    is_booking_order = fields.Boolean(
        string='Is Booking Order'
        )
    team = fields.Many2one(
        comodel_name='booking.service_team', 
        string='Team',
        )
    team_leader = fields.Many2one(
        comodel_name='booking.service_team', 
        string='Team Leader', 
        required=True
        )
    team_members = fields.Many2many(
        comodel_name='booking.service_team', 
        string='Team Members', 
        required=True
        )
    booking_start = fields.Datetime(
        string='Booking Start'
        )
    booking_end = fields.Datetime(
        string='Booking End'
        )

    @api.onchange('team')
    def onchange_team(self):
        search = self.env['booking.service_team'].search([('id','=', self.team.id)])
        team_members = []
        for team in search:
            team_members.extend(members.id for members in team.team_members)
            self.team_leader = team.team_members.id
            self.team_members = team_members
    
    def action_check(self):
        for check in self:
            wo = self.env['booking.work_order'].search(
                [('team_leader', 'in', [wo.id for wo in self.team_members]),
                 ('team_members','in', [self.team_leader.id]),
                 ('team_leader.', '=', self.team_leader.id),
                 ('team_members', 'in', [wo.id for wo in self.team_members]),
                 ('state', '!=', 'cancelled'),
                 ('planner_start', '<=', self.booking_start),
                 ('planner_end', '>=', self.booking_end),
                ],limit=1
            )
            if wo:
                raise ValidationError('Team already has work order during that period on SOXX')
            else:
                raise ValidationError('Team is available for booking')