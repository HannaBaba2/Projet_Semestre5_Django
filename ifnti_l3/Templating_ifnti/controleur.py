from jinja2 import Environment
from latex import build_pdf
from os.path import dirname, abspath, join

def generate_pdf(context, template_name="liste_eleves.tex", output_pdf=None):

    base_dir = dirname(dirname(abspath(__file__)))

    template_path = join(base_dir, "ifnti", template_name)

    out_dir = join(base_dir, "out")

    out_tex = join(out_dir, "template_out.tex")
    if output_pdf is None:
        output_pdf = template_name.replace(".tex", ".pdf")
    out_pdf = join(out_dir, output_pdf)

    j2_env = Environment(
        variable_start_string=r"\VAR{",
        variable_end_string="}",
        block_start_string=r"\BLOCK{",
        block_end_string="}",
        comment_start_string=r"\COMMENT{",
        comment_end_string="}"
    )

    with open(template_path, "r", encoding="utf-8") as fichier_in:
        template = fichier_in.read()

    monContext = context.copy()
    monContext["image_path"] = join(out_dir, "images") + "/"

    j2_template = j2_env.from_string(template)
    with open(out_tex, "w", encoding="utf-8") as fichier_out:
        fichier_out.write(j2_template.render(monContext))

    mon_pdf = build_pdf(open(out_tex, "r", encoding="utf-8"))
    mon_pdf.save_to(out_pdf)

    return out_pdf
