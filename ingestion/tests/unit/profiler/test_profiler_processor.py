#  Copyright 2021 Collate
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
Test Profiler Processor
"""

# Disabled as we'll need to rework this test entirely
# should be fixed in https://github.com/open-metadata/OpenMetadata/issues/5661
# from pytest import mark


# @mark.parametrize(
#     "condition,expected",
#     [
#         (None, None),
#     ],
# )
# def test_get_table_profile_sample(
#     condition,
#     expected,
#     base_orm_profiler_processor,
#     base_table,
# ):
#     processor = base_orm_profiler_processor

#     if condition:
#         ...

#     profile_sample = processor.get_table_profile_sample(
#         base_table,
#     )
#     assert profile_sample == expected
