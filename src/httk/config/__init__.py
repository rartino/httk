# 
#    The high-throughput toolkit (httk)
#    Copyright (C) 2012 - 2018 Rickard Armiento
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Read and setup httk configuration and versioning data. 

See docstring in config.py for more info.
"""

from .config import *
__doc__ = config.__doc__

# From this module
__all__ = ["config", "httk_root", "httk_python_root", "httk_version", "httk_version_date", "httk_copyright_note", "__version__", "__doc__"]
