const fs = require('fs');
const path = require('path');

const dbPath = path.join(__dirname, '../db.json');

function deleteProject(req, res) {
    const id = parseInt(req.params.id);
    
    fs.readFile(dbPath, (err, data) => {
        if (err) return res.status(500).send('Erreur serveur');

        const projects = JSON.parse(data);
        const index = projects.findIndex(p => p.id === id);

        if (index === -1) return res.status(404).send('Projet non trouvé');

        projects.splice(index, 1);

        fs.writeFile(dbPath, JSON.stringify(projects, null, 2), (err) => {
            if (err) return res.status(500).send('Erreur serveur');
            res.status(200).send({ message: 'Projet supprimé' });
        });
    });
}

module.exports = { deleteProject };
