import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import logging
from pathlib import Path

def create_heatmap(df, index='Product', columns='Month', values='SeverityScore'):
    """
    Create a heatmap visualization of escalation data.
    
    Args:
        df: DataFrame with escalation data
        index: Column to use for heatmap rows
        columns: Column to use for heatmap columns  
        values: Column to use for heatmap values
    """
    # Create pivot table for heatmap
    pivot_table = pd.pivot_table(df, index=index, columns=columns, values=values, aggfunc='sum', fill_value=0)
    
    # Set up the plot
    plt.figure(figsize=(12, 8))
    
    # Create heatmap with custom styling
    sns.heatmap(pivot_table, 
                annot=True, 
                cmap='Reds', 
                linewidths=0.5,
                fmt='g',
                cbar_kws={'label': 'Escalation Severity Score'})
    
    plt.title('EscaMap: Client Escalation Heatmap', fontsize=16, fontweight='bold', pad=20)
    plt.ylabel(index, fontsize=12)
    plt.xlabel(columns, fontsize=12)
    
    # SECURITY: Ensure static directory exists and validate path
    static_dir = Path('static')
    static_dir.mkdir(exist_ok=True)
    
    # SECURITY: Validate output path to prevent path traversal
    output_file = static_dir / 'escalation_heatmap.png'
    if not str(output_file.resolve()).startswith(str(static_dir.resolve())):
        raise ValueError("Invalid output path")
    
    # Save the plot
    plt.tight_layout()
    plt.savefig(str(output_file), dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory

def create_region_heatmap(df):
    """Create a heatmap showing escalations by region and severity."""
    pivot_table = pd.pivot_table(df, index='Region', columns='Severity', values='SeverityScore', aggfunc='count', fill_value=0)
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, 
                annot=True, 
                cmap='Blues', 
                linewidths=0.5,
                fmt='g',
                cbar_kws={'label': 'Number of Escalations'})
    
    plt.title('Escalations by Region and Severity', fontsize=14, fontweight='bold')
    plt.ylabel('Region', fontsize=12)
    plt.xlabel('Severity Level', fontsize=12)
    
    # SECURITY: Validate output path
    static_dir = Path('static')
    output_file = static_dir / 'region_heatmap.png'
    if not str(output_file.resolve()).startswith(str(static_dir.resolve())):
        raise ValueError("Invalid output path")
    
    plt.tight_layout()
    plt.savefig(str(output_file), dpi=300, bbox_inches='tight')
    plt.close()

def create_client_heatmap(df):
    """Create a heatmap showing escalations by client and product."""
    pivot_table = pd.pivot_table(df, index='Client', columns='Product', values='SeverityScore', aggfunc='sum', fill_value=0)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(pivot_table, 
                annot=True, 
                cmap='Oranges', 
                linewidths=0.5,
                fmt='g',
                cbar_kws={'label': 'Total Severity Score'})
    
    plt.title('Client Escalations by Product Area', fontsize=14, fontweight='bold')
    plt.ylabel('Client', fontsize=12)
    plt.xlabel('Product', fontsize=12)
    
    # SECURITY: Validate output path
    static_dir = Path('static')
    output_file = static_dir / 'client_heatmap.png'
    if not str(output_file.resolve()).startswith(str(static_dir.resolve())):
        raise ValueError("Invalid output path")
    
    plt.tight_layout()
    plt.savefig(str(output_file), dpi=300, bbox_inches='tight')
    plt.close()