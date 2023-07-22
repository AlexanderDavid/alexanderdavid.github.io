from pelican.plugins import render_math
import markdown.extensions.tables

# import pelican_cite

AUTHOR = "Alex Day"
SITENAME = "Alex Day"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

STATIC_PATHS = ["images", "pdfs", "extra"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

PLUGINS = [render_math]  # , pelican_cite]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Author Information
AUTHOR_TITLE = "Research Assistant @ Clemson University"
EMAIL = "alex@alexday.me"
PROFILE = "images/profile.jpg"

# Blogroll
LINKS = [
    ("LinkedIn", "https://www.linkedin.com/in/AlexanderDavidDay"),
    ("GitHub", "https://www.github.com/AlexanderDavid"),
    ("Resume", SITEURL + "/pdfs/day_resume.pdf"),
]

# Internal
INTERNAL = [("Home", "/"), ("Archives", "archives")]

ABOUT = [
    "I am a third year Ph.D. student at <a href='https://clemson.edu'>Clemson University</a> researching in the <a href='https://motion-lab.github.io/'>"
    + "Motion Planning Lab</a> under Dr. Ioannis Karamouzas. I got my B.S. in Computer Science from <a href='https://clarion.edu'>Clarion University</a> "
    + "(now WestPenn Clarion) in 2019. My passion for robotics started during an REU experience I had with the <a href='https://catvehicle.arizona.edu/'>"
    + "CAT Vehicle</a> team at the University of Arizona and has been fueled by the interesting projects in grad school as well as industry internships.",
    "My research interests revolve around motion planning wheeled robots (from Roombas to AVs) and I currently focus on human-robot interaction (HRI). "
    + "Outside of my research I am very bad at chess, Brazilian Jiu Jitsu, and climbing, but I am still in love with all three.",
]

# Experience
EXPERIENCE = [
    (
        "2020.08 - Present",
        "Research Assistant @ Clemson University Motion Planning Lab",
        "Advised by Dr. Ioannis Karamouzas",
    ),
    (
        "2020.08 - 2022.08",
        "Lead Graduate Teaching Assistant @ Clemson University",
        "Running, developing, and grading lab sessions for intro and intermediate Java/software development courses",
    ),
    (
        "Summer 2021, 2022, Winter 2021, 2022",
        "Software Engineering Intern @ Carnegie Robotics",
        "Wrote software and tested sensor calibration on a large autonomous robot platform",
    ),
    (
        "2020.05 - 2020.08",
        "Data Scientist (R&D) @ JGMS Inc.",
        "Developed deep learning for government document summarization and classification",
    ),
]

# Publications
PUBLICATIONS = [
    (
        "A Study in Zucker: Insights on Human-Robot Interactions",
        "images/zucker.png",
        ["Alex Day", "Ioannis Karamouzas"],
        [
            ["Paper", "https://arxiv.org/abs/2307.08668"],
            ["Dataset", "https://github.com/AlexanderDavid/ZuckerDataset"],
            ["Webpage", "/zucker-study"],
        ],
    ),
    (
        "COaaaNFET: An English Sentence to Emojis Translation Algorithm",
        "images/confet.png",
        ["Alex Day", "Chris Mankos", "Soo Kim", "Jody Strausser"],
        [
            [
                "Paper",
                "http://granite.sru.edu/~pacise/proceedings/pacise-proceedings-2020.pdf#page=61",
            ],
            ["Code", "https://github.com/AlexanderDavid/SentenceToEmojiTranslation"],
        ],
    ),
    (
        "A Comparison of Automatic Extractive Text Summarization Techniques",
        "images/comparison.png",
        ["Alex Day", "Soo Kim"],
        [
            [
                "Paper",
                "http://granite.sru.edu/~pacise/proceedings/pacise-proceedings-2019.pdf#page=98",
            ],
            [
                "Code",
                "https://github.com/AlexanderDavid/AutomaticExtractiveSummarization",
            ],
        ],
    ),
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# for bootstrap:
table_css_class = "table"

# class BetterMDTableProcessor(markdown.extensions.tables.TableProcessor):
#     def run(self, parent, blocks):
#         super().run(parent, blocks)
#         for e in parent:
#             if e.tag == 'table':
#                 e.attrib['class'] = table_css_class
#
# class BetterMDTableExtension(markdown.extensions.tables.TableExtension):
#     def extendMarkdown(self, md):
#         if '|' not in md.ESCAPED_CHARS:
#             md.ESCAPED_CHARS.append('|')
#         md.parser.blockprocessors.register(BetterMDTableProcessor(md.parser), 'table', 75)
#
# MARKDOWN = {
#     'extensions': [ BetterMDTableExtension() ],
#     'output_format': 'html5',
# }
