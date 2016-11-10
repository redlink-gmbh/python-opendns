# OpenDNS for Python

Small set of utilities to work with [OpenDNS](https://www.opendns.com/) from Python

# Setup

Stable version:

    pip install opendns
    
Development version:

    pip install .
    
# Usage

As a library:

    from opendns import get_ip
    print(get_ip())
    
As a CLI tool:

    $ opendns-getip 
    31.217.218.30

# License

Source code available under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0). The services
behind [OpenDNS](https://www.opendns.com/) are available under their own terms and conditions, so respect them.
