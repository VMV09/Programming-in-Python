from basic_programs.HelloWorld import helloworld

def test_helloworld():
  assert helloworld() == "Hello World, Python"
  assert helloworld(1) == "Hello World"
  assert helloworld(2) == "Hello Python"
