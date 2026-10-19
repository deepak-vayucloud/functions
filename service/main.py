import logging

from func_python.http import serve

logging.basicConfig(level=logging.INFO)

try:
    from function import new as handler  # type: ignore[import]
except ImportError:
    try:
        from function import handle as handler  # type: ignore[import]
    except ImportError:
        logging.error("Function must export either 'new' or 'handle'")
        raise


def main():
    logging.info("Functions middleware invoking user function")
    serve(handler)


if __name__ == "__main__":
    main()
