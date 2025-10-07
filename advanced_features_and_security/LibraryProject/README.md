# Permissions and Groups Setup

This project demonstrates how to use Django's permission system.

## Custom Permissions
Defined in `models.py`:
- can_view
- can_create
- can_edit
- can_delete

## Groups
- **Viewers:** can_view
- **Editors:** can_view, can_create, can_edit
- **Admins:** all permissions

## Views Protection
Each view checks permission using `@permission_required`.

## Testing
Create users and assign them to groups in Django Admin, then test access to each view.
