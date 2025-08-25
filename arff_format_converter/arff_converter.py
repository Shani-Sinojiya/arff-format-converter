"""Legacy entry point for ARFF converter - maintains backward compatibility."""

import sys
import argparse
from pathlib import Path

from .utils import main as legacy_main
from .cli import main as modern_main
from .__init__ import __version__


def main():
    """
    Main entry point that provides both legacy and modern CLI interfaces.

    This function maintains backward compatibility while providing access
    to the new modern CLI features.
    """
    try:
        # Check if we're being called with the old argument style
        if len(sys.argv) > 1:
            # Check for modern CLI commands
            modern_commands = {'convert', 'info', 'benchmark'}
            if sys.argv[1] in modern_commands:
                # Use modern CLI
                modern_main()
                return

            # Check for new-style arguments (using Path objects)
            if any(arg in sys.argv for arg in ['--parallel', '--chunk-size', '--verbose']):
                # Use modern CLI
                modern_main()
                return

        # Fall back to legacy interface for backward compatibility
        legacy_main()

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
