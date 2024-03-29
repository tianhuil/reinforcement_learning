from invoke import task


@task
def run_logistics(c, model_dir: str = "", input_advance: bool = False):
    from src.run_logistics import run_logistics_with_model

    run_logistics_with_model(model_dir=model_dir or None, input_advance=input_advance)


@task
def eval_logistics(c, model_dir: str = ""):
    from src.eval_logistics import eval_logistics_with_model

    eval_logistics_with_model(model_dir=model_dir or None)
