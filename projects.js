const express = require('express');
const router = express.Router();
const { deleteProject } = require('../controllers/projectsController');

// DELETE /projects/:id
router.delete('/:id', deleteProject);

module.exports = router;
