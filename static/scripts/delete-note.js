function deleteNote(noteId) {
    fetch(`/delete-note/${noteId}`, {  // Use backticks to insert the noteId into the URL
        method: "DELETE",  // Use DELETE method for deleting resources
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to delete note');
        }
        return response.json();  // Parse response JSON
    })
    .then(data => {
        // Handle successful deletion
        console.log(data.message);
        alert('Note deleted successfully!')
        window.location.href = "/";  // Redirect to homepage or desired location
    })
    .catch(error => {
        // Handle errors
        console.error('Error deleting note:', error);
        alert('error deleting note!')
        // Optionally, display an error message to the user
    });
}
