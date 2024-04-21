from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models import Note, db

deleteNote = Blueprint('deleteNote', __name__)


@deleteNote.route('/delete-note/<int:note_id>', methods=['DELETE'])
@login_required
def delete_note(note_id):
    try:
        # Check if the current user owns the note
        note = Note.query.filter_by(id=note_id, user_id=current_user.id).first()

        if note:
            # Delete the note from the database
            db.session.delete(note)
            db.session.commit()
            return jsonify({'message': 'Note deleted successfully'}), 200
        else:
            return jsonify({'error': 'Note not found or unauthorized'}), 404
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of an error
        return jsonify({'error': str(e)}), 500
