import streamlit as st
from PIL import Image
import base64
import io

# Set page configuration
st.set_page_config(
    page_title="Jerim Owino - Writing Portfolio",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS
st.markdown("""
<style>
:root {
    --primary: #2c3e50;
    --secondary: #3498db;
    --accent: #e74c3c;
    --light: #ecf0f1;
    --dark: #2c3e50;
    --gray: #95a5a6;
    --transition: all 0.3s ease;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.stApp {
    background-color: #f9f9f9;
    font-family: 'Merriweather', serif;
    line-height: 1.6;
    color: #333;
    overflow-x: hidden;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    margin-bottom: 1rem;
    color: var(--dark);
}

h1 {
    font-size: 3.5rem;
    line-height: 1.2;
}

h2 {
    font-size: 2.5rem;
    position: relative;
    margin-bottom: 3rem;
}

h2:after {
    content: '';
    position: absolute;
    bottom: -15px;
    left: 0;
    width: 80px;
    height: 4px;
    background: var(--accent);
}

.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.btn {
    display: inline-block;
    padding: 12px 30px;
    background: var(--secondary);
    color: white;
    text-decoration: none;
    border-radius: 4px;
    font-weight: 600;
    transition: var(--transition);
    border: none;
    cursor: pointer;
    font-size: 1rem;
    font-family: 'Montserrat', sans-serif;
}

.btn:hover {
    background: #2980b9;
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.btn-outline {
    background: transparent;
    border: 2px solid var(--secondary);
    color: var(--secondary);
}

.btn-outline:hover {
    background: var(--secondary);
    color: white;
}

/* Header Styles */
header {
    background-color: white;
    box-shadow: 0 2px 15px rgba(0,0,0,0.1);
    position: fixed;
    width: 100%;
    z-index: 1000;
    top: 0;
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 0;
    max-width: 1200px;
    margin: 0 auto;
    width: 90%;
}

.logo {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--primary);
    text-decoration: none;
    font-family: 'Montserrat', sans-serif;
}

.logo span {
    color: var(--accent);
}

.nav-links {
    display: flex;
    list-style: none;
}

.nav-links li {
    margin-left: 30px;
}

.nav-links a {
    text-decoration: none;
    color: var(--dark);
    font-weight: 500;
    font-size: 1.05rem;
    transition: var(--transition);
    font-family: 'Montserrat', sans-serif;
}

.nav-links a:hover {
    color: var(--accent);
}

/* Hero Section */
.hero {
    padding: 180px 0 100px;
    background: linear-gradient(135deg, rgba(44, 62, 80, 0.9) 0%, rgba(52, 152, 219, 0.8) 100%), url('https://images.unsplash.com/photo-1455390582262-044cdead277a?ixlib=rb-4.0.3') no-repeat center center/cover;
    color: white;
    text-align: center;
}

.hero h1 {
    color: white;
    margin-bottom: 20px;
}

.hero p {
    font-size: 1.4rem;
    max-width: 700px;
    margin: 0 auto 40px;
    font-weight: 300;
}

/* About Section */
.about {
    padding: 100px 0;
    background-color: white;
}

.about-content {
    display: flex;
    align-items: center;
    gap: 50px;
}

.about-text {
    flex: 1;
}

.about-image {
    flex: 1;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.about-image img {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.5s ease;
}

.about-image:hover img {
    transform: scale(1.05);
}

/* Skills Section */
.skills {
    padding: 100px 0;
    background-color: var(--light);
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    margin-top: 50px;
}

.skill-card {
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    transition: var(--transition);
    text-align: center;
}

.skill-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
}

.skill-icon {
    font-size: 3rem;
    color: var(--secondary);
    margin-bottom: 20px;
}

/* Projects Section */
.projects {
    padding: 100px 0;
    background-color: white;
}

.projects-filter {
    display: flex;
    justify-content: center;
    margin-bottom: 40px;
    flex-wrap: wrap;
}

.filter-btn {
    background: none;
    border: none;
    padding: 8px 20px;
    margin: 5px;
    cursor: pointer;
    font-family: 'Montserrat', sans-serif;
    font-weight: 500;
    border-radius: 30px;
    transition: var(--transition);
}

.filter-btn.active, .filter-btn:hover {
    background: var(--secondary);
    color: white;
}

.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 30px;
}

.project-card {
    background: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    transition: var(--transition);
}

.project-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
}

.project-image {
    height: 250px;
    overflow: hidden;
}

.project-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: var(--transition);
}

.project-card:hover .project-image img {
    transform: scale(1.1);
}

.project-content {
    padding: 25px;
}

.project-tags {
    display: flex;
    margin-bottom: 15px;
    flex-wrap: wrap;
}

.project-tag {
    background: var(--light);
    color: var(--secondary);
    padding: 5px 15px;
    border-radius: 30px;
    font-size: 0.85rem;
    margin-right: 10px;
    margin-bottom: 10px;
}

/* Contact Section */
.contact {
    padding: 100px 0;
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    color: white;
    text-align: center;
}

.contact h2 {
    color: white;
}

.contact h2:after {
    background: white;
    left: 50%;
    transform: translateX(-50%);
}

.contact p {
    max-width: 700px;
    margin: 0 auto 40px;
    font-size: 1.1rem;
}

/* Footer */
footer {
    background: var(--dark);
    color: white;
    padding: 50px 0 20px;
    text-align: center;
}

.social-links {
    display: flex;
    justify-content: center;
    margin-bottom: 30px;
}

.social-links a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: rgba(255,255,255,0.1);
    color: white;
    margin: 0 10px;
    font-size: 1.2rem;
    transition: var(--transition);
    text-decoration: none;
}

.social-links a:hover {
    background: var(--secondary);
    transform: translateY(-5px);
}

.copyright {
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.1);
    font-size: 0.9rem;
    color: var(--gray);
}

/* Responsive Design */
@media (max-width: 992px) {
    .about-content {
        flex-direction: column;
    }
    
    .hero {
        padding: 150px 0 80px;
    }
    
    h1 {
        font-size: 2.8rem;
    }
    
    h2 {
        font-size: 2.2rem;
    }
}

@media (max-width: 768px) {
    .nav-links {
        display: none;
    }
    
    .projects-grid {
        grid-template-columns: 1fr;
    }
    
    .hero {
        padding: 130px 0 60px;
    }
    
    h1 {
        font-size: 2.3rem;
    }
    
    h2 {
        font-size: 1.8rem;
    }
    
    .hero p {
        font-size: 1.1rem;
    }
    
    .nav-container {
        flex-direction: column;
        text-align: center;
    }
    
    .nav-links {
        margin-top: 20px;
        flex-direction: column;
    }
    
    .nav-links li {
        margin: 10px 0;
    }
}

/* Streamlit specific overrides */
.st-emotion-cache-1v0mbdj {
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.stButton>button {
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Header/Navigation
st.markdown("""
<header>
    <div class="nav-container">
        <a href="#" class="logo">Jerim<span>Owino</span></a>
        <ul class="nav-links">
            <li><a href="#about">About</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </div>
</header>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<section class="hero">
    <div class="container">
        <h1>Crafting Words That Captivate & Inspire</h1>
        <p>Professional writer specializing in compelling narratives, persuasive content, and engaging storytelling across multiple genres and platforms.</p>
        <a href="#projects" class="btn">View My Work</a>
    </div>
</section>
""", unsafe_allow_html=True)

# About Section
st.markdown("""
<section id="about" class="about">
    <div class="container">
        <h2>About Me</h2>
        <div class="about-content">
            <div class="about-text">
                <p>Hello! I'm Jerim Owino, a passionate writer with over 5 years of experience creating compelling content across various genres. My journey with words began as a child captivated by stories, evolving into a professional craft that I've honed through years of dedicated practice.</p>
                <p>I believe in the transformative power of language to educate, persuade, and inspire. My approach combines meticulous research with creative storytelling to produce content that resonates with diverse audiences.</p>
                <p>When I'm not crafting narratives, you'll find me exploring nature trails, reading classic literature, or conducting writing workshops for aspiring authors.</p>
                <div style="margin-top: 30px;">
                    <a href="#contact" class="btn btn-outline" style="margin-right: 15px;">Hire Me</a>
                    <a href="#" class="btn">Download CV</a>
                </div>
            </div>
            <div class="about-image">
                <img src="https://images.unsplash.com/photo-1543269865-cbf427effbad?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80" alt="Jerim Owino">
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Skills Section
st.markdown("""
<section id="skills" class="skills">
    <div class="container">
        <h2>My Writing Expertise</h2>
        <div class="skills-grid">
            <div class="skill-card">
                <div class="skill-icon">
                    <i class="fas fa-book"></i>
                </div>
                <h3>Creative Writing</h3>
                <p>Crafting compelling fiction, poetry, and narrative nonfiction that engages readers emotionally.</p>
            </div>
            <div class="skill-card">
                <div class="skill-icon">
                    <i class="fas fa-bullhorn"></i>
                </div>
                <h3>Content Marketing</h3>
                <p>Creating persuasive copy that drives engagement and conversions for brands and businesses.</p>
            </div>
            <div class="skill-card">
                <div class="skill-icon">
                    <i class="fas fa-file-alt"></i>
                </div>
                <h3>Technical Writing</h3>
                <p>Translating complex information into clear, accessible documentation and guides.</p>
            </div>
            <div class="skill-card">
                <div class="skill-icon">
                    <i class="fas fa-globe"></i>
                </div>
                <h3>SEO Writing</h3>
                <p>Optimizing content for search engines while maintaining readability and value for users.</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Projects Section
st.markdown("""
<section id="projects" class="projects">
    <div class="container">
        <h2>Featured Writing Projects</h2>
        <div class="projects-filter">
            <button class="filter-btn active">All</button>
            <button class="filter-btn">Fiction</button>
            <button class="filter-btn">Non-Fiction</button>
            <button class="filter-btn">Articles</button>
            <button class="filter-btn">Marketing</button>
        </div>
        <div class="projects-grid">
            <div class="project-card">
                <div class="project-image">
                    <img src="https://images.unsplash.com/photo-1544947950-fa07a98d237f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=774&q=80" alt="Project Image">
                </div>
                <div class="project-content">
                    <div class="project-tags">
                        <span class="project-tag">Fiction</span>
                        <span class="project-tag">Novel</span>
                    </div>
                    <h3>The Whispering Pines</h3>
                    <p>A psychological thriller novel exploring themes of memory and identity in a remote mountain town.</p>
                    <a href="#" class="btn btn-outline" style="margin-top: 15px;">Read Excerpt</a>
                </div>
            </div>
            <div class="project-card">
                <div class="project-image">
                    <img src="https://images.unsplash.com/photo-1506784983877-45594efa4cbe?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=776&q=80" alt="Project Image">
                </div>
                <div class="project-content">
                    <div class="project-tags">
                        <span class="project-tag">Marketing</span>
                        <span class="project-tag">Branding</span>
                    </div>
                    <h3>EcoSolutions Campaign</h3>
                    <p>Complete rebranding and content strategy for a sustainable products company.</p>
                    <a href="#" class="btn btn-outline" style="margin-top: 15px;">View Case Study</a>
                </div>
            </div>
            <div class="project-card">
                <div class="project-image">
                    <img src="https://images.unsplash.com/photo-1455390582262-044cdead277a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80" alt="Project Image">
                </div>
                <div class="project-content">
                    <div class="project-tags">
                        <span class="project-tag">Articles</span>
                        <span class="project-tag">Travel</span>
                    </div>
                    <h3>Hidden Europe Series</h3>
                    <p>12-part travelogue exploring lesser-known destinations across Eastern Europe.</p>
                    <a href="#" class="btn btn-outline" style="margin-top: 15px;">Read Articles</a>
                </div>
            </div>
            <div class="project-card">
                <div class="project-image">
                    <img src="https://images.unsplash.com/photo-1462823985959-022de68638a2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80" alt="Project Image">
                </div>
                <div class="project-content">
                    <div class="project-tags">
                        <span class="project-tag">Non-Fiction</span>
                        <span class="project-tag">Biography</span>
                    </div>
                    <h3>Pioneers of Science</h3>
                    <p>Biographical collection highlighting overlooked women in scientific history.</p>
                    <a href="#" class="btn btn-outline" style="margin-top: 15px;">View Project</a>
                </div>
            </div>
            <div class="project-card">
                <div class="project-image">
                    <img src="https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1774&q=80" alt="Project Image">
                </div>
                <div class="project-content">
                    <div class="project-tags">
                        <span class="project-tag">Technical</span>
                        <span class="project-tag">Documentation</span>
                    </div>
                    <h3>CloudSync API Guide</h3>
                    <p>Comprehensive technical documentation for a cloud storage integration platform.</p>
                    <a href="#" class="btn btn-outline" style="margin-top: 15px;">View Samples</a>
                </div>
            </div>
            <div class="project-card">
                <div class="project-image">
                    <img src="https://images.unsplash.com/photo-1584824486539-53bb4646bdbc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=774&q=80" alt="Project Image">
                </div>
                <div class="project-content">
                    <div class="project-tags">
                        <span class="project-tag">Blogging</span>
                        <span class="project-tag">SEO</span>
                    </div>
                    <h3>Digital Marketing Insights</h3>
                    <p>Ongoing blog series analyzing content strategy and SEO best practices.</p>
                    <a href="#" class="btn btn-outline" style="margin-top: 15px;">Visit Blog</a>
                </div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Contact Section
st.markdown(f"""
<section id="contact" class="contact">
    <div class="container">
        <h2>Let's Work Together</h2>
        <p>Have a writing project in mind? I'm currently accepting new clients for freelance work, collaborations, and speaking engagements. Reach out and let's create something remarkable.</p>
        <a href="mailto:owinojerim269@gmail.com" class="btn">Get in Touch</a>
    </div>
</section>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<footer>
    <div class="container">
        <div class="social-links">
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
            <a href="#"><i class="fab fa-medium"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
        </div>
        <p class="copyright">© 2023 Jerim Owino. All rights reserved.</p>
    </div>
</footer>
""", unsafe_allow_html=True)

# Font Awesome for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)

# JavaScript for interactivity
st.markdown("""
<script>
// Simple filter functionality for project categories
document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // In a real implementation, you would filter projects here
        });
    });
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
</script>
""", unsafe_allow_html=True)
