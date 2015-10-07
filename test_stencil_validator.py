import unittest
from stencil_validator import StencilValidator

class TestStencilValidator(unittest.TestCase):

  def test_black_lives_matter_is_invalid(self):
    validator = StencilValidator('test-stencils/invalid-black-lives-matter-stencil.png')
    self.assertFalse(validator.valid())

  def test_digital_heart_is_invalid(self):
    validator = StencilValidator('test-stencils/invalid-digital-heart-stencil.png')
    self.assertFalse(validator.valid())

  def test_end_mass_surveillance_is_invalid(self):
    validator = StencilValidator('test-stencils/invalid-end-mass-surveillance-stencil.png')
    self.assertFalse(validator.valid())

  def test_another_black_lives_matter_is_valid(self):
    validator = StencilValidator('test-stencils/valid-black-lives-matter-stencil.png')
    self.assertTrue(validator.valid())

  def test_another_digital_heart_is_valid(self):
    validator = StencilValidator('test-stencils/valid-digital-heart-stencil.png')
    self.assertTrue(validator.valid())

  def test_end_mass_surveillance_is_valid(self):
    validator = StencilValidator('test-stencils/valid-end-mass-surveillance-stencil.png')
    self.assertTrue(validator.valid())

if __name__ == '__main__':
    unittest.main()
