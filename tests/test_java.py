def test_java_exists(Command):
    version_result = Command("java -version")

    assert version_result.rc == 0
