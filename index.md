---
layout: landing
title: "Podcast del Doctor"
description: "Podcast sobre programació i tecnologia. Contingut generat amb IA per fomentar l'esperit crític i el debat tècnic."
---

<header class="header">
    <nav class="nav">
        <a href="#" class="logo"><i data-feather="home"></i> Podcast del Doctor</a>
        <ul class="nav-links">
            <li><a href="#about">Sobre el podcast</a></li>
            <li><a href="#disclaimer">Disclaimer</a></li>
            <li><a href="#subscribe">Subscriu-te</a></li>
            <li><a href="{{ '/episodis' | relative_url }}">Episodis</a></li>
        </ul>
        <button class="hamburger" onclick="toggleMobileMenu()" aria-label="Menú">
            <span></span>
            <span></span>
            <span></span>
        </button>
    </nav>
    <div class="mobile-menu" id="mobileMenu">
        <a href="#about"><i data-feather="book"></i> Sobre el podcast</a>
        <a href="#disclaimer"><i data-feather="alert-circle"></i> Disclaimer</a>
        <a href="#subscribe"><i data-feather="smartphone"></i> Subscriu-te</a>
        <a href="{{ '/episodis' | relative_url }}"><i data-feather="headphones"></i> Tots els Episodis</a>
    </div>
</header>

<main>
    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <img src="{{ '/assets/logo-podcast.jpg' | relative_url }}" alt="Logo Podcast del Doctor" class="podcast-logo">
            <h1>Podcast del Doctor</h1>
            <p class="subtitle">Programació i tecnologia amb esperit crític</p>
            <p class="description">
                Explorant el món de la programació, les noves tecnologies i la intel·ligència artificial.
                Contingut generat amb IA per fomentar el debat tècnic i el pensament crític.
            </p>
            <div class="cta-buttons">
                <a href="podcast://david-rodenas.com/podcast-del-doctor/feed.xml" class="btn btn-apple">
                    <i data-feather="headphones"></i> Apple Podcasts
                </a>
                <!-- <a href="#" target="_blank" rel="noopener" class="btn btn-spotify">
                    <i data-feather="radio"></i> Spotify
                </a> -->
                <a href="#subscribe" class="btn btn-primary">
                    <i data-feather="plus"></i> Més opcions
                </a>
            </div>
        </div>
    </section>

    <!-- Últims Episodis Section -->
    <section id="latest-episodes" class="latest-episodes fade-in">
        <div class="container">
            <h2 class="section-title"><i data-feather="mic"></i> Últims Episodis</h2>
            <p class="section-subtitle">Escolta directament des del navegador o subscriu-te per rebre'ls automàticament</p>

            {% assign sorted_episodes = site.episodes | sort: 'date' | reverse %}
            {% assign latest_episodes = sorted_episodes | slice: 0, 3 %}

            <div class="latest-grid">
                {% for episode in latest_episodes %}
                <article class="latest-card">
                    <div class="latest-number">{{ episode.episode_number | default: forloop.index }}</div>
                    <div class="latest-content">
                        <h3><a href="{{ episode.url | relative_url }}">{{ episode.title }}</a></h3>
                        <div class="latest-meta">
                            <time>{{ episode.date | date: "%d/%m/%Y" }}</time>
                            {% if episode.duration %}<span class="latest-duration">{{ episode.duration }}</span>{% endif %}
                        </div>
                        {% if episode.audio_file %}
                        <div class="latest-player">
                            <audio controls preload="none">
                                {% if episode.audio_file contains "http" %}
                                <source src="{{ episode.audio_file }}" type="audio/mpeg">
                                {% else %}
                                <source src="{{ '/episodes/' | append: episode.audio_file | relative_url }}" type="audio/mpeg">
                                {% endif %}
                            </audio>
                        </div>
                        {% endif %}
                        <a href="{{ episode.url | relative_url }}" class="latest-link">Veure detalls →</a>
                    </div>
                </article>
                {% endfor %}
            </div>

            <div class="all-episodes-cta">
                <a href="{{ '/episodis' | relative_url }}" class="btn btn-primary btn-large">
                    <i data-feather="book"></i> Veure tots els episodis ({{ sorted_episodes.size }})
                </a>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about fade-in">
        <div class="container">
            <h2 class="section-title">Què és aquest podcast?</h2>
            <div class="about-grid">
                <div class="about-card">
                    <div class="icon"><i data-feather="code"></i></div>
                    <h3>Programació</h3>
                    <p>Explorem llenguatges, patrons de disseny i bones pràctiques del desenvolupament de software.</p>
                </div>
                <div class="about-card">
                    <div class="icon"><i data-feather="layers"></i></div>
                    <h3>Arquitectura</h3>
                    <p>Analitzem decisions d'arquitectura, microserveis, monòlits i tot el que hi ha entremig.</p>
                </div>
                <div class="about-card">
                    <div class="icon"><i data-feather="cpu"></i></div>
                    <h3>100% Generat amb IA</h3>
                    <p>Intel·ligència artificial per fomentar el debat crític. No som una font de veritat absoluta.</p>
                </div>
                <div class="about-card">
                    <div class="icon"><i data-feather="link"></i></div>
                    <h3>Fonts Transparents</h3>
                    <p>Sempre proporcionem les fonts originals perquè puguis consultar la informació directament.</p>
                </div>
                <div class="about-card">
                    <div class="icon"><i data-feather="clock"></i></div>
                    <h3>Episodis Curts</h3>
                    <p>Programes de ~10 minuts, perfectes per aprendre coses noves sense perdre temps.</p>
                </div>
                <div class="about-card">
                    <div class="icon"><i data-feather="zap"></i></div>
                    <h3>Tecnologia</h3>
                    <p>Frameworks, eines, IA, DevOps i tot el que mou el món del desenvolupament.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Disclaimer Section -->
    <section id="disclaimer" class="disclaimer fade-in">
        <div class="disclaimer-content">
            <h2><i data-feather="alert-circle"></i> Esperit Crític i Transparència</h2>
            <p>
                Aquest podcast està <strong>completament generat amb intel·ligència artificial</strong>.
            </p>
            <p>
                <strong>L'objectiu NO és presentar veritats absolutes</strong>,
                sinó <strong>fomentar l'esperit crític</strong> presentant diferents perspectives i conceptes
                sobre programació i tecnologia.
            </p>
            <p>
                <strong>Et convidem a buscar la veritat per tu mateix.</strong>
                Sempre proporcionem les fonts originals perquè puguis:
            </p>
            <ul>
                <li><i data-feather="check-circle"></i> Contrastar la informació directament</li>
                <li><i data-feather="check-circle"></i> Formar-te la teva pròpia opinió</li>
                <li><i data-feather="check-circle"></i> Qüestionar tant el nostre contingut com les fonts oficials</li>
                <li><i data-feather="check-circle"></i> Participar activament en el debat públic</li>
            </ul>
            <p>
                <strong>Recorda:</strong> La IA pot contenir interpretacions, biaixos o errors.
                El pensament crític i la verificació independent són sempre essencials.
            </p>
        </div>
    </section>

    <!-- Subscribe Section -->
    <section id="subscribe" class="subscribe fade-in">
        <div class="container">
            <h2><i data-feather="smartphone"></i> Subscriu-te al Podcast</h2>
            <p>Escolta quan vulguis i rep els nous episodis automàticament</p>

            <!-- Opcions principals -->
            <div class="subscribe-main-options">
                <div class="subscribe-option-card">
                    <div class="option-icon"><i data-feather="globe"></i></div>
                    <h3>Escoltar aquí</h3>
                    <p>No cal instal·lar res</p>
                    <a href="{{ '/episodis' | relative_url }}" class="subscribe-btn listen-btn">
                        <i data-feather="play"></i> Escoltar ara
                    </a>
                </div>

                <div class="subscribe-option-card">
                    <div class="option-icon"><i data-feather="smartphone"></i></div>
                    <h3>Subscriu-te amb l'App</h3>
                    <p>Detecta les teves apps de podcasts</p>
                    <a href="https://www.subscribeonandroid.com/david-rodenas.com/podcast-del-doctor/feed.xml"
                       target="_blank" rel="noopener" class="subscribe-btn app-btn">
                        <i data-feather="download"></i> Subscriu-te ara
                    </a>
                </div>

                <div class="subscribe-option-card">
                    <div class="option-icon"><i data-feather="list"></i></div>
                    <h3>Afegir manualment</h3>
                    <p>Copia l'URL RSS</p>
                    <button onclick="copyRSSNoAlert()" class="subscribe-btn copy-btn-action">
                        <i data-feather="clipboard"></i> Copiar URL
                    </button>
                </div>
            </div>

            <!-- Instruccions ràpides -->
            <details class="quick-instructions">
                <summary><i data-feather="settings"></i> Com afegir un podcast manualment?</summary>
                <div class="instructions-content">
                    <p><strong>URL del Feed RSS:</strong></p>
                    <code class="rss-display">{{ site.url }}{{ site.baseurl }}/feed.xml</code>
                    <ol>
                        <li>Copia l'URL de dalt</li>
                        <li>Obre la teva app de podcasts (Apple Podcasts, Pocket Casts, AntennaPod...)</li>
                        <li>Busca "Afegir per URL" o "Add by RSS"</li>
                        <li>Enganxa l'URL i subscriu-te</li>
                    </ol>
                    <p class="note"><i data-feather="alert-circle"></i> Spotify no suporta RSS externs. Utilitza una altra app.</p>
                </div>
            </details>
        </div>
    </section>
</main>

<!-- Footer -->
<footer class="footer">
    <div class="container">
        <div class="footer-links">
            <a href="#about">Sobre el podcast</a>
            <a href="#disclaimer">Disclaimer</a>
            <a href="https://david-rodenas.com" target="_blank">david-rodenas.com</a>
            <a href="{{ '/feed.xml' | relative_url }}">RSS</a>
            <a href="https://github.com/drpicox/podcast-del-doctor">GitHub</a>
        </div>
        <p>&copy; {{ 'now' | date: '%Y' }} David Rodenas</p>
        <p><small>Contingut generat amb IA • Fomenta l'esperit crític • CC BY 4.0</small></p>
    </div>
</footer>