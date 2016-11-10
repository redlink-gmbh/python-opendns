# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import subprocess


def get_ip():
    proc = subprocess.Popen(["dig", "+short", "myip.opendns.com", "@resolver1.opendns.com"], stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    return out.strip().decode("utf-8")


def print_ip():
    print(get_ip())
