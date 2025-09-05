#!/usr/bin/env python
"""
Simple test script to verify URL routing and reverse lookups
"""
import os
import sys
import django
from django.conf import settings

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'akins_blog.settings')
django.setup()

from django.urls import reverse, resolve
from django.test import TestCase
from What_readers_see.models import BlogPost
from django.contrib.auth.models import User


def test_url_patterns():
    """Test URL patterns and reverse lookups"""
    print("Testing URL patterns...")
    
    # Test blog list URL
    try:
        list_url = reverse('What_readers_see:blog_list')
        print(f"✓ Blog list URL: {list_url}")
        
        # Test resolving the URL
        resolved = resolve(list_url)
        print(f"✓ Blog list resolves to: {resolved.view_name}")
    except Exception as e:
        print(f"✗ Blog list URL error: {e}")
    
    # Test blog detail URL with sample slug
    try:
        detail_url = reverse('What_readers_see:blog_detail', kwargs={'slug': 'sample-post'})
        print(f"✓ Blog detail URL: {detail_url}")
        
        # Test resolving the URL
        resolved = resolve(detail_url)
        print(f"✓ Blog detail resolves to: {resolved.view_name}")
        print(f"✓ Blog detail slug parameter: {resolved.kwargs}")
    except Exception as e:
        print(f"✗ Blog detail URL error: {e}")
    
    # Test URL patterns from root
    try:
        root_list = reverse('What_readers_see:blog_list')
        root_detail = reverse('What_readers_see:blog_detail', kwargs={'slug': 'test-slug'})
        print(f"✓ Root blog list: {root_list}")
        print(f"✓ Root blog detail: {root_detail}")
    except Exception as e:
        print(f"✗ Root URL error: {e}")


def test_model_url_method():
    """Test BlogPost get_absolute_url method"""
    print("\nTesting BlogPost get_absolute_url method...")
    
    try:
        # Create a test user (won't be saved to database)
        user = User(username='testuser', email='test@example.com')
        
        # Create a test blog post (won't be saved to database)
        post = BlogPost(
            title='Test Post',
            slug='test-post',
            content='Test content',
            excerpt='Test excerpt',
            author=user,
            published=True
        )
        
        # Test get_absolute_url method
        url = post.get_absolute_url()
        print(f"✓ BlogPost.get_absolute_url(): {url}")
        
        # Verify it matches our URL pattern
        expected_url = reverse('What_readers_see:blog_detail', kwargs={'slug': 'test-post'})
        if url == expected_url:
            print(f"✓ URL matches expected pattern: {expected_url}")
        else:
            print(f"✗ URL mismatch. Got: {url}, Expected: {expected_url}")
            
    except Exception as e:
        print(f"✗ Model URL method error: {e}")


if __name__ == '__main__':
    test_url_patterns()
    test_model_url_method()
    print("\nURL configuration testing complete!")