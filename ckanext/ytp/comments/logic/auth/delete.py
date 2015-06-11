import logging
from pylons.i18n import _

import ckan.new_authz as new_authz
from ckan import logic
import ckanext.ytp.comments.model as comment_model


log = logging.getLogger(__name__)


def comment_delete(context, data_dict):
    model = context['model']
    user = context['user']

    userobj = model.User.get(user)

    cid = logic.get_or_bust(data_dict, 'id')

    comment = comment_model.Comment.get(cid)
    if not comment:
        return {'success': False, 'msg': _('Comment does not exist')}

    # if sysadmin.
    if new_authz.is_sysadmin(user):
        return {'success': True}

    # if package owner / organization owner
    if logic.check_access('package_update', context, data_dict):
        log.debug("HERE WE GO!")
        return {'success': True}

    if comment.user_id != userobj.id:
        return {'success': False, 'msg': _('User is not the author of the comment')}

    return {'success': True}
