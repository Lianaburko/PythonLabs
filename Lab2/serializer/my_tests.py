import unittest
import serializer.examples as examples
from serializer.factory import Factory

class SerializeTester(unittest.TestCase):
    def test_json_int(self):
        self.s = Factory.create_serializer('.json')
        old_obj = examples.a
        new_obj = self.s.loads(self.s.dumps(old_obj,2,0))
        self.assertEqual(old_obj, new_obj)

    def test_json_function_butoma(self):
        self.s = Factory.create_serializer('.json')
        old_obj = examples.butoma
        new_obj = self.s.loads(self.s.dumps(old_obj,2,0))
        self.assertEqual(old_obj(2,4), new_obj(2,4))
    
    def test_json_function_recursia(self):
        self.s = Factory.create_serializer('.json')
        old_obj = examples.recusia
        new_obj = self.s.loads(self.s.dumps(old_obj,2,0))
        self.assertEqual(old_obj(5), new_obj(5))
    
    def test_json_class_tree(self):
        self.s = Factory.create_serializer('.json')
        old_obj = examples.Tree
        new_obj = self.s.loads(self.s.dumps(old_obj,2,0))
        tree_1 = new_obj("oak", 0.5)
        tree_2 = old_obj("oak", 0.5)

        self.assertEqual(tree_1.info(), tree_2.info())

    def test_json_class_Fruittree(self):
        self.s = Factory.create_serializer('.json')
        old_obj = examples.FruitTree
        new_obj = self.s.loads(self.s.dumps(old_obj,2,0))
        tree_1 = new_obj("apple", 0.5)
        tree_2 = old_obj("apple", 0.5)
        self.assertEqual(tree_1.info(), tree_2.info())

    def test_json_class_Fruittree_grow(self):
        self.s = Factory.create_serializer('.json')
        old_obj = examples.FruitTree
        new_obj = self.s.loads(self.s.dumps(old_obj,2,0))
        tree_1 = new_obj("apple", 0.5)
        tree_1.grow()
        self.assertEqual(tree_1.height, 1)

    def test_json_class_object(self):
        self.s = Factory.create_serializer('.json')
        old_obj = examples.vasya
        new_obj = self.s.loads(self.s.dumps(old_obj,2,0))
        inf1 = old_obj.display_count()
        inf2 = new_obj.display_count(new_obj)
        self.assertEqual(inf1, inf2)
    



    def test_toml_int(self):
        self.s = Factory.create_serializer('.toml')
        old_obj = examples.a
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_function_butoma(self):
        self.s = Factory.create_serializer('.toml')
        old_obj = examples.butoma
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(2,4), new_obj(2,4))
    
    def test_toml_function_recursia(self):
        self.s = Factory.create_serializer('.toml')
        old_obj = examples.recusia
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(5), new_obj(5))
    
    def test_toml_class_tree(self):
        self.s = Factory.create_serializer('.toml')
        old_obj = examples.Tree
        new_obj = self.s.loads(self.s.dumps(old_obj))
        tree_1 = new_obj("oak", 0.5)
        tree_2 = old_obj("oak", 0.5)
        self.assertEqual(tree_1.info(), tree_2.info())

    def test_toml_class_Fruittree_grow(self):
        self.s = Factory.create_serializer('.toml')
        old_obj = examples.FruitTree
        new_obj = self.s.loads(self.s.dumps(old_obj))
        tree_1 = new_obj("apple", 0.5)
        tree_1.grow()
        self.assertEqual(tree_1.height, 1)

    def test_toml_class_Fruittree(self):
        self.s = Factory.create_serializer('.toml')
        old_obj = examples.FruitTree
        new_obj = self.s.loads(self.s.dumps(old_obj))
        tree_1 = new_obj("apple", 0.5)
        tree_2 = old_obj("apple", 0.5)
        self.assertEqual(tree_1.info(), tree_2.info())

    def test_toml_class_object(self):
        self.s = Factory.create_serializer('.toml')
        old_obj = examples.vasya
        new_obj = self.s.loads(self.s.dumps(old_obj))
        inf1 = old_obj.display_count()
        inf2 = new_obj.display_count(new_obj)
        self.assertEqual(inf1, inf2)




    def test_yaml_int(self):
        self.s = Factory.create_serializer('.yaml')
        old_obj = examples.a
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_function_butoma(self):
        self.s = Factory.create_serializer('.yaml')
        old_obj = examples.butoma
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(2,4), new_obj(2,4))
    
    def test_yaml_function_recursia(self):
        self.s = Factory.create_serializer('.yaml')
        old_obj = examples.recusia
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(5), new_obj(5))
    
    def test_yaml_class_tree(self):
        self.s = Factory.create_serializer('.yaml')
        old_obj = examples.Tree
        new_obj = self.s.loads(self.s.dumps(old_obj))
        tree_1 = new_obj("oak", 0.5)
        tree_2 = old_obj("oak", 0.5)

        self.assertEqual(tree_1.info(), tree_2.info())

    def test_yaml_class_Fruittree(self):
        self.s = Factory.create_serializer('.yaml')
        old_obj = examples.FruitTree
        new_obj = self.s.loads(self.s.dumps(old_obj))
        tree_1 = new_obj("apple", 0.5)
        tree_2 = old_obj("apple", 0.5)
        self.assertEqual(tree_1.info(), tree_2.info())

    def test_yaml_class_Fruittree_grow(self):
        self.s = Factory.create_serializer('.yaml')
        old_obj = examples.FruitTree
        new_obj = self.s.loads(self.s.dumps(old_obj))
        tree_1 = new_obj("apple", 0.5)
        tree_1.grow()
        self.assertEqual(tree_1.height, 1)

    def test_yaml_class_object(self):
        self.s = Factory.create_serializer('.yaml')
        old_obj = examples.vasya
        new_obj = self.s.loads(self.s.dumps(old_obj))
        inf1 = old_obj.display_count()
        inf2 = new_obj.display_count(new_obj)
        self.assertEqual(inf1, inf2)


if __name__ == '__main__':
    unittest.main()