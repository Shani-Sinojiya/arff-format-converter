#!/usr/bin/env python3
"""
Generate test data for ARFF Format Converter benchmarks
"""

import tempfile
from pathlib import Path

def generate_test_arff(output_path, num_rows=1000):
    """Generate a simple test ARFF file."""
    
    arff_content = f"""@relation test_data

@attribute feature1 numeric
@attribute feature2 numeric
@attribute feature3 string
@attribute class {{positive,negative}}

@data
"""
    
    # Add sample data rows
    for i in range(num_rows):
        feature1 = i * 0.1
        feature2 = (i % 100) * 0.5
        feature3 = f"text_{i % 10}"
        class_val = "positive" if i % 2 == 0 else "negative"
        arff_content += f"{feature1},{feature2},{feature3},{class_val}\n"
    
    with open(output_path, 'w') as f:
        f.write(arff_content)
    
    print(f"✅ Generated test ARFF file: {output_path} ({num_rows} rows)")

def main():
    """Generate test data files."""
    try:
        test_data_dir = Path("test_data")
        test_data_dir.mkdir(exist_ok=True)
        
        # Generate different sized test files
        sizes = [1000, 10000, 50000]
        
        print(f"🚀 Starting test data generation...")
        print(f"📁 Output directory: {test_data_dir}")
        
        for size in sizes:
            output_file = test_data_dir / f"test_data_{size}.arff"
            print(f"📝 Generating {size} rows...")
            generate_test_arff(output_file, size)
        
        print(f"🎯 Generated {len(sizes)} test files in {test_data_dir}")
        print(f"✅ Test data generation completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during test data generation: {e}")
        import traceback
        traceback.print_exc()
        import sys
        sys.exit(1)

if __name__ == '__main__':
    main()
