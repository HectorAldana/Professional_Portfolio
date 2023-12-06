document.addEventListener('DOMContentLoaded', function() {
    const projects = [
        { name: "Matrices & Linear Systems - 2D Rotation", description: "Linear Transformation in R2 space.", slug: "Calculus-1" },
        { name: "Matrices & Linear Systems - 3D Rotation", description: "Linear Transformation in R3 space." , slug: "Calculus-2" },
        { name: "Matrices & Linear Systems - Eigenvalue Problem", description: "Application in facial recognition.", slug: "Calculus-3"  },
        { name: "Matrix Eigenvalue Problem", description: "High dimensional dataset & dimensionality reduction with Principal Component Analysis.", slug: "Calculus-4"  },
        { name: "Vector Differential Calculus - Gradient Descent", description: "Minimizing a cost function in a linear regression model.", slug: "Calculus-5"  },
        { name: "Gradient, Divergence, and Curl - Visualizations", description: "Simulations of vector fields.", slug: "Calculus-5"  },
        { name: "Green's Integral Theorem, Gauss and Stokes Theorems", description: "Simulation of electromagnetic fields.", slug: "Calculus-6"  },
        { name: "Cauchy-Riemann Equations and Complex Trigonometric Functions", description: "Visualizing how these functions transform the complex plane.", slug: "Calculus-6"  },
        { name: "Power Series and Laurent Series", description: "Series expansions of functions' demo.", slug: "Calculus-7"  },
        { name: "Residue Integration Method", description: "Application involving complex integration in the context of signal processing.", slug: "Calculus-8"  },
        { name: "Conformal Mappings", description: "Visual demo of conformal mapping effects.", slug: "Calculus-9"  },
        // Add more projects here
    ];

    const projectsContainer = document.querySelector('.projects-container');

    projects.forEach(project => {
        const projectElement = document.createElement('div');
        projectElement.classList.add('project-item');
        projectElement.innerHTML = `<h3>${project.name}</h3><p class="project-description">${project.description}</p>`;
        projectsContainer.appendChild(projectElement);

        projectElement.addEventListener('click', () => {
            window.location.href = `ProjectItems/${project.slug}.html`;
        });
    });
});
