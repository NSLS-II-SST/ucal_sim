from setuptools import setup, find_packages

setup(
    author="Charles Titus",
    author_email="charles.titus@nist.gov",
    install_requires=["bluesky", "ophyd"],
    name="sst_common_sim",
    entry_points = {"sst_common": ["sst_sim = sst_common_sim.api"]},
    use_scm_version=True,
    packages=find_packages()
)
