import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import AutomationCenter from '../pages/AutomationCenter'

describe('AutomationCenter UI', () => {
  it('renders registered workflows section', () => {
    render(<AutomationCenter />)
    expect(screen.getByText(/Registered Workflows/i)).toBeTruthy()
    expect(screen.getByText(/daily-expo-watch/i)).toBeTruthy()
  })
})
